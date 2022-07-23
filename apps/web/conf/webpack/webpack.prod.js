const path = require('path');
const Dotenv = require('dotenv-webpack');
const { DefinePlugin } = require( 'webpack' );

module.exports = {
    mode: 'production',
    plugins: [
        new DefinePlugin({
            IS_DESKTOP_BUILD: JSON.stringify(false),
        }),
        new Dotenv({
            path: path.resolve(__dirname, '.env.production')
        }),
    ],
    devServer: {
        static: {
            directory: path.resolve(__dirname, '..', '..', './build')
        }
    }
}
