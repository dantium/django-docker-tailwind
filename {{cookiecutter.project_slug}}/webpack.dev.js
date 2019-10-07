const merge = require('webpack-merge');
const common = require('./webpack.common.js');


module.exports = merge(common, {
   mode: 'development',
   watch: true,
   watchOptions: {
      aggregateTimeout: 300,
      poll: 1000,
      ignored: ['/node_modules/']
  },
});
