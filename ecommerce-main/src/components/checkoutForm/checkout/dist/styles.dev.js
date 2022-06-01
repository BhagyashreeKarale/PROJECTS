"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _styles = require("@material-ui/core/styles");

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var _default = (0, _styles.makeStyles)(function (theme) {
  var _paper;

  return {
    appBar: {
      position: 'relative'
    },
    toolbar: theme.mixins.toolbar,
    layout: _defineProperty({
      marginTop: '5%',
      width: 'auto',
      marginLeft: theme.spacing(2),
      marginRight: theme.spacing(2)
    }, theme.breakpoints.up(600 + theme.spacing(2) * 2), {
      width: 600,
      marginLeft: 'auto',
      marginRight: 'auto'
    }),
    paper: (_paper = {
      marginTop: theme.spacing(3),
      marginBottom: theme.spacing(3),
      padding: theme.spacing(2)
    }, _defineProperty(_paper, theme.breakpoints.down('xs'), {
      width: '100%',
      marginTop: 60
    }), _defineProperty(_paper, theme.breakpoints.up(600 + theme.spacing(3) * 2), {
      marginTop: theme.spacing(6),
      marginBottom: theme.spacing(6),
      padding: theme.spacing(3)
    }), _paper),
    stepper: {
      padding: theme.spacing(3, 0, 5)
    },
    buttons: {
      display: 'flex',
      justifyContent: 'flex-end'
    },
    button: {
      marginTop: theme.spacing(3),
      marginLeft: theme.spacing(1)
    },
    divider: {
      margin: '20px 0'
    },
    spinner: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    }
  };
});

exports["default"] = _default;