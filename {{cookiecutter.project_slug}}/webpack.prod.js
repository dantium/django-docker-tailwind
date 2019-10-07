const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const glob = require("glob-all");
const path = require('path');
const PurgecssPlugin = require("purgecss-webpack-plugin");
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')


class TailwindExtractor {
  static extract(content) {
    return content.match(/[A-Za-z0-9-_:\/]+/g) || [];
  }
}

const purgecss = new PurgecssPlugin({
  paths: glob.sync([
    //path.join(__dirname, "{{ cookiecutter.project_slug }}/static/js/**/*.vue"),
    path.join(__dirname, "{{ cookiecutter.project_slug }}/templates/**/*.html"),
    path.join(__dirname, "{{ cookiecutter.project_slug }}/static/js/*.js")
  ]),
  extractors: [
    {
      extractor: TailwindExtractor,
      extensions: ["html", "js", "vue"]
    }
  ],
  whitelist: ['a']
})

const favicon = new FaviconsWebpackPlugin({
  logo: path.resolve(__dirname, '{{ cookiecutter.project_slug }}/static/images/logo.svg'),
  //outputPath: path.resolve(__dirname, 'favicon/'),
  prefix: 'favicon/',
});

module.exports = merge(common, {
    mode: 'production',
    plugins: [purgecss, favicon],
    optimization: {
        minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    },
});
