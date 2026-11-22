# MD2PDF Lab Notes

## Challenge Description

Hello Hacker!

TopTierConversions LTD is proud to announce its latest and greatest product launch: MD2PDF.

This easy-to-use utility converts markdown files to PDF and is totally secure! Right...?

## Initial Reconnaissance

We start without a link to the web page, so we run an Nmap scan to identify open ports. Ports 80 and 5000 are open. Port 80 is used for HTTP.

We enter `http://IP` in the browser and access a page where we can convert text into a PDF.

First, we look at the page source, but we do not see anything useful:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <link
      rel="stylesheet"
      href="./static/codemirror.min.css"/>

    <link
      rel="stylesheet"
      href="./static/bootstrap.min.css"/>


    <title>MD2PDF</title>
  </head>

  <body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="/"><span class="">MD2PDF</span></a>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">
      <div class="">
        <div class="card mt-4">
          <textarea class="form-control" name="md" id="md"></textarea>
        </div>

        <div class="mt-3 d-grid gap-2 d-md-flex justify-content-md-end">
          <button id="convert" class="btn btn-primary" type="button">
            Convert to PDF
          </button>
        </div>
        <div class="mt-3">
          <div
            id="progress"
            class="progress"
            style="height: 30px; display: none"
          >
            <div
              class="progress-bar progress-bar-striped bg-success progress-bar-animated"
              role="progressbar"
              style="width: 100%"
              aria-valuenow="100"
              aria-valuemin="0"
              aria-valuemax="100"
            >
              Processing...
            </div>
          </div>
        </div>
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
  </body>
  <!-- jQuery CDN - Slim version (=without AJAX) -->
  <script
    src="./static/jquery-3.3.1.slim.min.js"></script>
  <!-- Bootstrap JS -->
  <script
    src="./static/bootstrap.bundle.min.js"></script>
  <!-- Custom -->
  <script
    src="./static/codemirror.min.js"></script>
  <script
    src="./static/markdown.js"></script>
  <script>
    $(document).ready(function () {
      var editor = CodeMirror.fromTextArea(document.getElementById("md"), {
        mode: "markdown",
        lineNumbers: true,
        tabSize: 2,
        lineWrapping: true,
      })
      $("#convert").click(function () {
        const data = new FormData()
        data.append("md", editor.getValue())
        $("#progress").show()

        fetch("/convert", {
          method: "POST",
          body: data,
        })
          .then((response) => response.blob())
          .then((data) => window.open(URL.createObjectURL(data)))
          .catch((error) => {
            $("#progress").hide()
            console.log(error)
          })
      })
    })
  </script>
</html>
```

## Conversion Script

This is the script that sends the Markdown to the server for conversion into a PDF.

The script sets up the markdown editor, sends its contents to the server, and opens the returned file.

```javascript
$(document).ready(function () {
  var editor = CodeMirror.fromTextArea(document.getElementById("md"), {
    mode: "markdown",
    lineNumbers: true,
    tabSize: 2,
    lineWrapping: true,
  })
})
```

It finds the `<textarea>` with `id="md"` and turns it into a CodeMirror editor.

The process goes like this:

```text
Markdown → POST /convert → server processes it → returned PDF
```

## HTML Rendering Test

To test the server, we try `<b>Hello</b>` to see whether it renders the text in bold. It does.

The server is processing HTML.
