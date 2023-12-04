<template>
  <div class="main">
    <div class="banner">
      <img alt="Vue logo" src="../assets/logo.png">
      <h1>StageStats</h1>
    </div>
    <div class="section-container">
      <section class="search">
        <h2>Search Artists</h2>
        <div class="search-container">
          <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Enter Artist Name" v-model="artistName">
      <button type="button" class="btn btn-primary" @click="searchArtist">Search</button>
    </div>
          <div class="filter-container">
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Filters
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a @click="toggleFilter($event)" class="dropdown-item" value="Year">Year</a>
                <a @click="toggleFilter($event)" class="dropdown-item" value="Album">Album</a>
                <a @click="toggleFilter($event)" class="dropdown-item" value="Tour">Tour</a>
                <a @click="toggleFilter($event)" class="dropdown-item" value="Venue">Venue</a>
              </div>
            </div>
            <div class="filter-btn" v-for="filter in filters" v-bind:key="filter"><span>{{ filter.message }}</span><img
                src="../assets/close-fill.svg" @click="removeFilter(filter)" /></div>
          </div>
          <div class="input-group mb-3" style="display: none;">
            <input type="text" class="form-control" placeholder="Year">
          </div>
          
        </div>
        <div class="show-buttons-container">
          <h3>Show:</h3>
          <div class="buttons">
            <button :class="{ 'btn-active': selectedButton === 'merge' }" @click="selectButton('merge')">Merge</button>
            <button :class="{ 'btn-active': selectedButton === 'quick' }" @click="selectButton('quick')">Quick</button>
          </div>
          <h4>Time Elapsed:</h4>
        </div>
        
      </section>
      <section class="content">
        <h2>Contents</h2>
        <p class="songs-header">Songs most played by:</p>
        <ul>
          <li v-for="setlist in searchResults" :key="setlist['artist_name']">{{ setlist['artist_name']}}</li>
        </ul>
      </section>
    </div>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'MainVue',
  data(){
    return {
      filters:[],
      selectedButton: '',
      artistName: '',
      searchResults: [],
      response: {},
    }
  },
  props: {
    msg: String
  },
  methods:{
    toggleFilter(event){
      var filtername = event.target.text;
      var existingFilter = this.filters.find(f => f.message === filtername);
      if (!existingFilter){
        this.filters.push({message: filtername});
      }
    },
    removeFilter(filterToRemove) {
      this.filters = this.filters.filter(filter => filter.message !== filterToRemove.message);
    },
    selectButton(button) {
      this.selectedButton = button;
    },
    async searchArtist() {
      const { data } = await axios.get(`http://127.0.0.1:8000/setlists/api?artist=${this.artistName}&format=json`);
      this.response = data;
      this.searchResults = data;
      console.log(JSON.parse(JSON.stringify(this.searchResults)));
      return JSON.parse(JSON.stringify(this.searchResults))  // this is just proof of concept
      //const url = `http://127.0.0.1:8000/setlists/api?artist=${this.artistName}/`; 
      // fetch(url)
      //   .then(response => {
      //     if (!response.ok) {
      //       throw new Error(`HTTP error! Status: ${response.status}`);
      //     }
      //     return response.json();
      //   })
      //   .then(data => {
      //     this.searchResults = data['artist_name'];
      //   })
      //   .catch(error => {
      //     console.error('Error fetching the artist data:', error);
      //   });
    },
    async getAnswer() {
      //const { data } = await axios.get("http://127.0.0.1:8000/setlists/api?format=json");
      //this.answer = data;
      //console.log(this.answer)
    },
    
  }
}
</script>

<style scoped>

.main {
  box-sizing: border-box;
  display: flex;
  flex-flow: column wrap;
  flex-grow: 1;
}

.banner {
  background-color: rgb(25, 28, 31);
  height: 7vh;
  display: flex;
  justify-content: center;
  flex-direction: row;
  overflow: hidden;
}

.banner h1{
  padding: 0;
  margin: 0;
  line-height: 6.4vh;
  flex-shrink: 1;
}

.banner img{
  flex-shrink: 1;
}
.section-container{
  display: flex;
  text-align: center;
  margin-top: 2vh;
  padding-bottom: 5vh;
  box-sizing: border-box;
  flex-grow: 1;
  flex-wrap: wrap;
}
.search{
  display: flex;
  flex-flow: column wrap;
  flex-basis: 20vw;
  background-color: rgb(36, 40, 44);
  border-radius: 2.5em;
  flex-grow: 1;
  margin-right: 1vh;
  margin-left: 1vh;
  box-sizing: border-box;
  position: relative;
}

.search h2{
  margin-top: 1vh;
}

.search .search-container{
  display: flex;
  flex-flow: column wrap;
  justify-content: space-around;
  padding-left: 3vh;
  padding-right: 3vh;
  box-sizing: border-box;
}

.filter-container{
  display: flex;
  flex-flow: row wrap;
  justify-content: flex-start;
  gap: 1vw;
  box-sizing: border-box;
}

.search .search-container .filter-container .dropdown{
  display: flex;
}

.filter-btn{
  display: flex;
  background-color: #0d6efd;
  border-radius: .5vh;
  position: relative;
  width: 5rem;
  height: 2.5rem;
  justify-content: center;
  align-items: center;
}

.filter-btn span{

}
.filter-btn img{
  width: 1.2rem;
  box-sizing: border-box;
  position: absolute;
  top:0px;
  right:0px;
}

.content{
  flex-basis: 30vw;
  padding-top: 15px;
  border: solid;
  border-color: rgb(0, 0, 0);
  flex-grow: 4;
  height: 100%;
  margin-right: 1vh;
  box-sizing: border-box;
  display: flex;
  
  flex-direction: column;
}
.show-buttons-container {
  display: flex;
  position: absolute;
  flex-direction: column;
  position: absolute;
  bottom: 0px;
  left: 1vw;
}
.show-buttons-container p {
  margin-bottom: 5px;
}
.buttons {
  display: flex;
  flex-direction: row;
  gap: 5px;
}
.buttons button {
  background-color: grey;
  color: white;
  margin-bottom: 12px;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.buttons .btn-active {
  background-color: green;
}


.content h2, .content .songs-header {
  display: inline-block;
  text-align: left;
  padding-left: 20px;
  
}

.content li{
  text-align: left;
}


</style>
