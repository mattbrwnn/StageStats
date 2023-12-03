<template>
  <!--<img alt="Vue logo" src="./assets/logo.png">-->
  <MainVue msg="Welcome to Your Vue.js App"/>
</template>

<script>
import MainVue from './components/Main.vue'

export default {
  name: 'App',
  components: {
    MainVue
  }
}
</script>

<style>
#app{
  min-height: 100vh;
  display: flex;
}
</style>
