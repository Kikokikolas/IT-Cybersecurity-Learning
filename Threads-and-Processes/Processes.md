# Processes and Threads in Linux

## 1. Programs and Processes

A **process** is a program in execution, together with the resources and state that the operating system (OS) needs to manage it while it is running.

Think of cooking:

- **Program:** A recipe stored in a file on disk.
- **Process:** Preparing that recipe in a kitchen at a particular moment, using resources such as RAM, CPU time, and files.
- **Thread:** A worker in that kitchen. Several workers can share the same resources while performing different tasks.

Multiple instances of the same program can run as separate processes, each with its own **process ID (PID)**. However, opening two application windows does not necessarily create two processes; this depends on the application.

## 2. What the Kernel Tracks

A **process control block (PCB)** is the general operating-system concept for the information used to manage a process. Linux represents tasks using structures such as `task_struct`, with references to other resource structures.

| Information | Meaning |
| --- | --- |
| PID | The process's own identifier. |
| PPID | The identifier of its parent process. |
| Credentials | User and group IDs used in permission checks. |
| VSZ | Virtual address-space size; this is not the amount of physical RAM occupied. |
| RSS | Resident set size: memory currently resident in RAM, including shared pages. |
| State | Whether a task is runnable, sleeping, stopped, or in another state. |
| Execution context | Information needed to resume execution, such as registers and the instruction pointer. |
| Open resources | File descriptors referring to files, sockets, and other objects. |

Common state letters include `R` (running or runnable), `S` (interruptible sleep), `D` (uninterruptible sleep), `T` (stopped), and `Z` (zombie: exited but not yet reaped).

Many of these details are exposed through `/proc/PID/status`. See the [Linux process-status documentation](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html).

## 3. Creating a Process: Fork and Exec

In Linux and Unix, a common way to launch a program has two steps:

1. **Fork:** `fork()` creates a child process with its own PID. Its PPID identifies the parent. Parent and child have separate address spaces, initially containing the same data. Linux uses **copy-on-write**, so it does not immediately duplicate every memory page.
2. **Exec:** The child can call an `exec`-family function to replace its current program. A successful `execve()` keeps the PID and replaces the process image; it does not create another process.

A child does not have to call `exec`: it can continue running the existing program. See the Linux manuals for [fork](https://man7.org/linux/man-pages/man2/fork.2.html) and [execve](https://man7.org/linux/man-pages/man2/execve.2.html).

## 4. How Bash Runs Commands

Bash is a process that reads and executes shell commands. A terminal emulator provides the window in which you interact with it; the terminal emulator and Bash are separate programs.

For an ordinary foreground external command such as `ls -l`, the conceptual sequence is:

1. **Read and parse:** Identify the command `ls` and its argument `-l`.
2. **Find the executable:** Resolve the command, normally using `$PATH`.
3. **Create a child:** Fork a child process.
4. **Execute:** The child replaces its program with `ls`.
5. **Wait and reap:** The parent shell waits for completion and collects the child's exit status before displaying another prompt.

```text
Bash (parent)
  ├── creates child → child executes ls → child exits
  └── waits for child → collects status → displays prompt
```

If you explicitly run `exec ls`, Bash replaces itself with `ls`. When `ls` exits, that shell is gone. Whether the terminal window closes depends on the terminal's settings.

See Bash's [command search and execution documentation](https://www.gnu.org/software/bash/manual/html_node/Command-Search-and-Execution.html).

### External Commands and Shell Builtins

| Type | Examples | Usual behavior for a simple foreground command |
| --- | --- | --- |
| External command | `ls`, `grep`, `python3`, `cat`, `/bin/echo` | Run in a separate process. |
| Shell builtin | `echo`, `cd`, `export`, `exit`, `pwd` | Run inside the shell process. |

Builtins such as `cd` and `export` can change the current shell's state. If a child changes its working directory, the parent's working directory stays unchanged. Builtins also avoid the overhead of launching an external command.

Pipelines, background jobs, and subshells can cause builtins to run in a separate execution environment. See Bash's [execution-environment documentation](https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html).

### Programs on Disk and in Memory

| Item | On disk | During execution |
| --- | --- | --- |
| Bash | An executable such as `/usr/bin/bash`, including its builtins. | A shell process with access to builtin implementations. |
| `ls` | A separate executable, commonly `/usr/bin/ls`. | Runs in a process when invoked. |
| Nmap | An installed executable, commonly `/usr/bin/nmap`. | Runs in a process when invoked. |

Paths vary by system. Loading a program does not mean that every byte is immediately read from disk into physical RAM; memory pages can be loaded on demand or obtained from a cache.

## 5. Installed Tools and Your Own Programs

### Nmap

Installing Nmap places its executable and supporting files on disk. When you run it from Bash, the shell resolves the command and launches it using the same general mechanism as other external programs. The parent shell normally waits for a foreground scan to finish.

### A Compiled C Program

```bash
gcc main.c -o my_program
./my_program
```

Compilation creates an executable. When you invoke it, the shell launches a process that executes the compiled program.

### A Python Script

```bash
python3 script.py
```

Here, the executable is the Python interpreter. It receives `script.py` as an argument and runs the script's instructions. CPython, the common Python implementation, is written primarily in C; other implementations exist.

An executable script can begin with:

```python
#!/usr/bin/env python3
```

When the script is executed directly, Linux recognizes the interpreter line and invokes `/usr/bin/env` with the appropriate arguments. `env` then finds and executes `python3`. This is interpreter handling during execution, not a separate process for every script instruction. See [interpreter scripts in execve](https://man7.org/linux/man-pages/man2/execve.2.html).

## 6. Desktop Applications and Browser Tabs

### Launching Spotify from the Desktop

Clicking an application icon requests that the application be launched or activated. On Linux desktops, a `.desktop` file commonly describes how to start it.

The exact parent process depends on the desktop environment and launch mechanism. A launcher or a user service manager may be involved; it is not always `gnome-shell` directly creating the process. The `systemd --user` manager is also distinct from the system manager running as PID 1.

### Chrome's Processes

Chromium uses several process roles:

| Role | Purpose |
| --- | --- |
| Browser | Coordinates browser behavior and manages browser-level UI. |
| Renderer | Executes web content and renders pages. |
| GPU | Handles graphics-related work. |
| Utility | Provides services such as networking and other isolated tasks. |

There is no fixed one-process-per-tab rule. Tabs can share renderers, and frames within a tab can use different renderer processes. Process separation supports fault containment and sandboxing. See Chromium's [multi-process architecture](https://new.chromium.org/developers/design-documents/multi-process-architecture/).

## 7. Processes and Threads Working Together

A music player can divide work among processes and threads. The following is an illustrative design, not a verified map of Spotify's internal architecture:

| Task | Possible responsibility |
| --- | --- |
| User interface | Respond to clicks and update the display. |
| Networking | Fetch audio data and other content. |
| Audio decoding | Convert encoded audio into samples. |
| Audio output | Deliver samples to the audio system. |

Pressing **Play** can signal existing workers; it does not inherently require a new process for each song.

The kitchen analogy helps explain resource sharing: processes usually have separate address spaces, while threads within one process share memory and resources. Each thread still has its own stack and execution state. Shared data requires synchronization, and an error in one thread can affect the whole process.

### Fork, Clone, and Threads

Linux provides `clone()` and `clone3()` interfaces with flags controlling resource sharing. The glibc `fork()` wrapper uses cloning machinery to provide fork semantics, while thread libraries use suitable sharing flags to create threads.

Sharing memory alone does not fully define a thread: thread-group membership and other resource-sharing settings matter too. It is inaccurate to say that Linux has replaced every process-creation interface with one identical `clone()` call. See [clone and clone3](https://man7.org/linux/man-pages/man2/clone.2.html).

In a thread listing, repeated process IDs with different **LWP** or thread IDs indicate multiple threads in one process. They do not, by themselves, show that all those threads belong to one browser tab.

## 8. Where the First Processes Come From

Booting starts before there is a shell available to launch commands. A typical Linux boot sequence is:

1. **Firmware:** BIOS or UEFI initializes hardware and selects a boot target.
2. **Bootloader:** A loader such as GRUB loads the kernel and, commonly, an initramfs. Some configurations allow firmware to load a kernel directly.
3. **Kernel initialization:** Linux initializes its core facilities and starts the first user-space task, PID 1. The kernel itself is not an ordinary user-space process called “PID 0.”
4. **Early user space:** When an initramfs is used, its `/init` prepares access to the real root filesystem. PID 1 can begin here, before that filesystem is mounted.
5. **System initialization:** Control passes to the main init system, commonly systemd. It starts services; login and user-session components subsequently launch desktop applications.

User services such as a desktop audio server may be managed by a per-user service manager. The exact process tree depends on the system configuration.

See the [systemd boot overview](https://www.freedesktop.org/software/systemd/man/latest/bootup.html) and the kernel's [early user-space documentation](https://docs.kernel.org/driver-api/early-userspace/early_userspace_support.html).
