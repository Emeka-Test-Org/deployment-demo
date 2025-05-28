// vulnerable.js
const http = require('http');
const url = require('url');

// 🔥 This is unsafe and should trigger CodeQL alert
http.createServer(function (req, res) {
  const query = url.parse(req.url, true).query;
  const input = query.input;
  eval(input);  // 🚨 DANGEROUS: triggers CodeQL alert for arbitrary code execution
  res.end('Executed');
}).listen(3000);
