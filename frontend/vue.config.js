// vue.config.js
const path = require('path');
const webpack = require('webpack')
function resolve(dir) {
    return path.join(__dirname, dir)
}
module.exports = {
    lintOnSave: false,
    chainWebpack: config => {
        //路径配置
        config.resolve.alias
            .set('@', resolve('./'))
            .set('assets', resolve('src/assets'))
            .set('styles', resolve('src/assets/styles'))
    },
    // webpack-dev-server 相关配置  
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                "windows.jQuery": "jquery"
            })
        ]
    },
    devServer: {
        port: 8080,
        // proxy: {
        //     '/api': {
        //       target: 'http://localhost:5000/', //对应自己的接口
        //       changeOrigin: true,
        //       ws: true,
        //       pathRewrite: {
        //         '^/api': ''
        //       }
        //     }
        //   }
    },
    publicPath: "",
}