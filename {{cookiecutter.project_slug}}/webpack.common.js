const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const styleRule = {
  test: /\.pcss$/,
  use: [
    MiniCssExtractPlugin.loader,
    //{loader: 'style-loader'},
    { loader: 'css-loader', options: { sourceMap: true, importLoaders: 1 } },
    {loader: 'postcss-loader'}
    //'sass-loader'
  ]
};

const cssRule = {
  test: /\.css$/,
  use: [MiniCssExtractPlugin.loader, 'css-loader']
}

const assetRule = {
  test: /.(jpg|png|woff(2)?|eot|ttf|svg)$/,
  loader: 'file-loader'
};

const jsRule = {
  test: /\.m?js$/,
  exclude: /(node_modules|bower_components)/,
  use: {
    loader: 'babel-loader',
    options: {
      presets: ['@babel/preset-env']
    }
  }
};


module.exports = {
    context: __dirname,

    entry: ['./{{ cookiecutter.project_slug }}/src/js/main.js', './{{ cookiecutter.project_slug }}/src/css/main.pcss'],
    output: {
        filename: 'js/main.js',
        chunkFilename: '[name]-[hash].js',
        path: path.resolve(__dirname, '{{ cookiecutter.project_slug }}/static')
    },
    resolve: {
      mainFields: ['browser', 'module', 'main']
    },
    module: {
      rules: [styleRule, cssRule] },

    plugins: [
        new MiniCssExtractPlugin({
          filename: 'css/[name].css',

        }),
    ],
};
