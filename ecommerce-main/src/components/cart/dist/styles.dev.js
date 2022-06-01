"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _core = require("@material-ui/core");

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var _default = (0, _core.makeStyles)(function (theme) {
  var _emptyButton;

  return {
    toolbar: theme.mixins.toolbar,
    title: {
      marginTop: '5%'
    },
    emptyButton: (_emptyButton = {
      minWidth: '150px'
    }, _defineProperty(_emptyButton, theme.breakpoints.down('xs'), {
      marginBottom: '5px'
    }), _defineProperty(_emptyButton, theme.breakpoints.up('xs'), {
      marginRight: '20px'
    }), _emptyButton),
    checkoutButton: {
      minWidth: '150px'
    },
    link: {
      textDecoration: 'none'
    },
    cardDetails: {
      display: 'flex',
      marginTop: '10%',
      width: '100%',
      justifyContent: 'space-between'
    }
  };
});

exports["default"] = _default;