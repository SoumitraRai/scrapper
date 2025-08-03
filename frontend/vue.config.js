module.exports = {
  devServer: {
    host: '0.0.0.0',
    proxy: {
      '/api': {
        target: 'http://localhost:5000',  // redirect to Flask App
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''  // Remove /api prefix when forwarding to backend
        }
      }
    }
  }
}