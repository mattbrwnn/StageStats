<template>
  <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
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
          <select class="form-select form-select-lg mb-3 filter-select" v-for="filter in filters" v-bind:key="filter" aria-label=".form-select-lg example">
            <option selected>{{filter.message}}</option>
            <template v-if="filter.message === 'Album'">
              <option v-for="album in albums" v-bind:key="album" value="1">{{ album['name'] }}</option>
            </template>
            
          </select>
          
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
        <p class="songs-header">Songs most played by: {{ artistName }}</p>
        <ul class="song-list">
          <li v-for="(count, song) in searchResults" :key="song">{{ song }}: {{ count }}</li>
        </ul>
        <!-- <ul>
          <li v-for="setlist in searchResults" :key="setlist['artist_name']">{{ setlist['artist_name']}}</li>
        </ul> -->
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
      albums: [],
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
      var { data } = await axios.get(`http://127.0.0.1:8000/setlists/api?artist=${this.artistName}&format=json`);
      this.albums = data['albums'];
      delete data['albums'];
      this.searchResults = data;
      console.log(data)
      var json = JSON.parse(JSON.stringify(this.albums));
      console.log(json);
      return json // this is just proof of concept


    }
    
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
  max-height: 750px;
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
  max-height: 700px;
  overflow-y: auto;
  flex-direction: column;
}
.song-list {
  list-style: none;
  padding-left: 20px;
}

.song-list li {
  margin: 5px 0;
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

.filter-select{
margin-top: 1vh;
--bs-form-select-bg-img: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='white' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e");
background-color: #424242;
border-color: #363636;
color: #363636;
}

</style>
