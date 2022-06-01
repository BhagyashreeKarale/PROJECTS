"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _core = require("@material-ui/core");

var _default = (0, _core.makeStyles)(function (theme) {
  return {
    toolbar: theme.mixins.toolbar,
    content: {
      flexGrow: 1,
      backgroundColor: theme.palette.background["default"],
      padding: theme.spacing(3)
    },
    root: {
      flexGrow: 1
    }
  };
});

exports["default"] = _default;