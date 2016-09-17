#!/usr/bin/env node
'use strict'

const vorpal = require('vorpal')();
const SerialPort = require("serialport");
const _ = require("lodash");
const Promise = require("bluebird");

let port;

const listPort = () => {
	return new Promise((res,rej) => {
		SerialPort.list((err, ports) => {
			if (err) rej(err);

			let ports_active = [];
			_.each(ports, function(port) {
				if (port.manufacturer) ports_active.push(port);
			})
			res(ports_active);
		});
	})
}

vorpal
	.command('list', 'List ports open')
	.action(function(args, callback) {
		listPort()
			.then((ports) => {
				this.log('Active ports : ');
				ports.forEach((port) => {
					this.log('COM : '+port.comName);
				})
				callback();
			});
	});

vorpal
	.command('connect <port>', 'Connect to <port>')
	.action(function(args, callback) {
		port = new SerialPort.SerialPort("/dev/ttyUSB0", {
			baudRate: 57600
		});
		callback();
	});

vorpal
	.command('write <command>', 'Write <command> to port')
	.action(function(args, callback) {
		let that = this;
		if (port) {
			port.write(args.command, function(err) {
			  if (err) {
			    return that.log('Error on write: ', err.message);
			  }
			  that.log('message written');
			});
		} else {
			this.log('connect port first');
		}
		callback();
	});

vorpal
	.command('close', 'Close connection on open port')
	.action(function(args, callback) {
		
		callback();
	});

vorpal
	.command('status', 'See connection status')
	.action(function(args, callback) {
		
		callback();
	});

vorpal
	.delimiter('efishery$')
	.show();