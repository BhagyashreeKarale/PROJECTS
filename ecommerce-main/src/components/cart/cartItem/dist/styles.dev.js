"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _styles = require("@material-ui/core/styles");

var _default = (0, _styles.makeStyles)(function () {
  return {
    media: {
      height: 260
    },
    cardContent: {
      display: 'flex',
      justifyContent: 'space-between'
    },
    cartActions: {
      justifyContent: 'space-between'
    },
    buttons: {
      display: 'flex',
      alignItems: 'center'
    }
  };
});

exports["default"] = _default;