const isProd = process.env.NODE_ENV === 'production'

export default {
  namespaced: true,
  state: {
    USE_HTTPS: isProd,
    BACKEND_API_HOST: '127.0.0.1',
    BACKEND_API_PORT: 8000
  },
  getters: {
    BACKEND_API_ADDRESS: (state) => {
      return (state.USE_HTTPS ? 'https://' : 'http://') + state.BACKEND_API_HOST + ':' + state.BACKEND_API_PORT
    }
  }
}
