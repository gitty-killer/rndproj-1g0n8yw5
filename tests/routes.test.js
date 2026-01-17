"use strict";

const assert = require("assert");
const { handleRequest } = require("../src/router");

function mockReq(url, method, body) {
  const listeners = {};
  return {
    url,
    method,
    on: (event, cb) => { listeners[event] = cb; if (event === "end") { cb(); } },
    _body: body || ""
  };
}

function mockRes() {
  return {
    status: null,
    headers: null,
    body: "",
    writeHead: function(status, headers) { this.status = status; this.headers = headers; },
    end: function(data) { this.body = data || ""; }
  };
}

const res = mockRes();
handleRequest({ url: "/status", method: "GET", on: () => {} }, res);
assert.strictEqual(res.status, 200);
