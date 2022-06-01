"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.commerce = void 0;

var _commerce = _interopRequireDefault(require("@chec/commerce.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var commerce = new _commerce["default"](process.env.REACT_APP_CHEC_PUBLIC_KEY, true);
exports.commerce = commerce;