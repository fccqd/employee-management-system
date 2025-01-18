const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      css: {
        modules: {
          localIdentName: '[name]-[hash]'
        }
      }
    }
  },
  // 定义 Vue 特性标志
  chainWebpack: config => {
    config.plugin('define').tap(args => {
      args[0]['process.env'].VUE_PROD_HYDRATION_MISMATCH_DETAILS = true;
      return args;
    });
  }
})
