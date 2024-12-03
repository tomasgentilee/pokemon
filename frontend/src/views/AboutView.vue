<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      pokemon: [],
    }
  },
  mounted() {
    this.fetchPokemon()
  },
  methods: {
    fetchPokemon() {
      const pokeid = this.$route.params.pokeid
        .get(`pokemon/${pokeid}`, {
        })
        .then(response => {
          this.pokemon = response.data;
          console.log(this.pokemon)
        })
    },
  },
}
</script>

<template>
    <header>
    <nav class="navbar">
      <div class="logo" ></div>
      <router-link to="#" class="nav-link">Home</router-link>
    </nav>
  </header>


  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<style>
</style>
