<template>
  <div id="app">
    <EmployeeList/>
  </div>
</template>

<script>
import EmployeeList from './components/EmployeeList.vue'

export default {
  name: 'App',
  components: {
    EmployeeList
  }
}
</script>

<style scoped>
/* {
  box-sizing: border-box;
} */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>