#!/usr/bin/env node

var org = require("./org");
var parser = new org.Parser();

process.stdin.resume();
process.stdin.setEncoding('utf8');

var orgCode = "";
process.stdin.on('data', function (chunk) {
  orgCode += chunk;
});

process.stdin.on('end', function () {
  parseAndOutputHTML();
});

function parseAndOutputHTML() {
  var orgDocument = parser.parse(orgCode);
  var orgHTMLDocument = orgDocument.convert(org.ConverterHTML, {});
  console.log(orgHTMLDocument.toString());
}
