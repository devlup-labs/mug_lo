import Vue from 'vue'
import LogIn from '../../../src/pages/login'

describe('LogIn.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(LogIn)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.hello h1').textContent)
      .to.equal('<W></W>elcome to Your Vue.js PWA')
  })
})
