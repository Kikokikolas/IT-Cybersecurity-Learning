# Sources

Sources is the panel where you inspect the actual files and code that the browser has loaded, especially JavaScript.

Elements -> what does the current DOM look like?

Console -> what is JavaScript doing / what errors are happening?

Sources -> which source files did the browser load, and where is the code running?

When you open Sources, you will normally see several areas.

Sources
│
├── Page
│   ├── HTML files
│   ├── JavaScript files
│   ├── CSS files
│   └── other loaded resources
│
├── Code editor
│   └── shows the selected file
│
└── Debugging tools
    ├── Breakpoints
    ├── Call Stack
    ├── Scope
    └── Watch

The most important part initially is Page. There, we can browse the resources that came from the current page and sometimes from third-party domains.

For example:

example.com
│
├── index.html
├── main.js
├── app.js
└── style.css

googleapis.com
└── some-library.js

This shows that the browser did not necessarily receive everything from a single server. Modern pages commonly load scripts, fonts, analytics, APIs, and other resources from multiple domains.

This JavaScript was delivered to the browser and can therefore be inspected.

This reinforces something we discussed earlier:

Server-side source code
        ↓
usually remains on the server

Client-side JavaScript
        ↓
sent to browser
        ↓
can be inspected in Sources

Production JavaScript often looks horrible, though:

(()=>{var a=1,b=function(c){return c+1};...

That is often because the code has been minified or bundled to reduce file size.