<template>
  <div class="app">
    <Header label="Исторический тест" />
    <BodyTest />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import BodyTest from './components/Bodytest.vue';

export default {
  name: 'Historical Test',
  components: {
    Header,
    BodyTest
  }
}
</script>

<style>
</style>
