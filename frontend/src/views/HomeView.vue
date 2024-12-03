<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      pokemons: [],
    }
  },
  mounted() {
    this.fetchPokemons()
  },
  methods: {
    fetchPokemons() {
      let pags = this.$route.params.pags
      axios
        .get(`pokemons/${pags}`, {
        })
        .then(response => {
          this.pokemons = response.data;
          console.log(this.pokemons)
        })
    },
    //getPokemonId(url) {
    //  console.log(url)
    //}
    // next50(pags){
    //   pags+=50
    // },
    // prev50(pags){
    //   pags+=50
    // }
  },
}
</script>

<template>
  <main>
    <header>
    <nav class="navbar">
      <img src="../assets/logosc.png" width="150" height="50">
      <router-link to="#" class="nav-link">Home</router-link>
    </nav>
  </header>

  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Ver</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="pokemon in this.pokemons">
        <td>{{ pokemon.name }}</td>
        <td> {{ pokemon.url }}</td>
      </tr>
    </tbody>
  </table>
  <button>anterior</button>
  <button>siguiente</button>

  </main>
</template>
