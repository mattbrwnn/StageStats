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
        </div>
        <div class="show-buttons-container">
          <h3>Show:</h3>
          <div class="buttons">
            <button :class="{ 'btn-active': selectedButton === 'merge' }" @click="selectButton('merge')">Merge</button>
            <button :class="{ 'btn-active': selectedButton === 'quick' }" @click="selectButton('quick')">Quick</button>
          </div>
          <h4>Time Elapsed: {{ timeElapsed }}</h4>
        </div>
        
      </section>
      <section class="content">
        <h2>Contents</h2>
        <p class="songs-header">Songs most played by: {{ artistName }}</p>
        <ul class="song-list">
          <li v-for="(item, index) in searchResults" :key="index">{{ index + 1 }}. "{{ item[0] }}" - {{ item[1] }}</li>
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
      selectedButton: '',
      artistName: '',
      searchResults: [],
      response: {},
      timeElapsed: null,
    }
  },
  props: {
    msg: String
  },
  methods:{   
    // Makes a request to our DjangoAPI backend to retrieve the songs and their associated play counts
    async searchArtist() {
      var { data } = await axios.get(`http://127.0.0.1:8000/setlists/api?artist=${this.artistName}&format=json`);
      this.searchResults = this.shuffle(
        Object.entries(data).map(([song, count]) => [song, parseInt(count)])
      );
      return this.searchResults},

     // Shuffles the song data for sorting because the data came pre sorted 
    shuffle(data) {
      for (let i = data.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [data[i], data[j]] = [data[j], data[i]]; 
      }
      return data;
    },
    // Defines behavior for sort buttons to request the data to be sorted by the backend and returned to the frontend
    async selectButton(button) {
      this.selectedButton = button;
      let endpoint = '';
      switch (button) {
        case 'quick':
          endpoint = 'quick-sort';
          break;
        case 'merge':
          endpoint = 'merge-sort';
          break;
      }
      if (endpoint) {
        try {
          // sends request to API to sort the song data
          const response = await axios.post(`http://127.0.0.1:8000/setlists/${endpoint}`, { list: this.searchResults });
          this.searchResults = response.data.sorted_data;
          this.timeElapsed = response.data.time_elapsed;
          console.log(this.searchResults)
        } 
        // Catches error if API request fails
        catch (error) {
          console.error('Error making the sorting request:', error);
        }

      }
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
  align-items: flex-start;
  bottom: 300px;
  left: 1vw;
}
.show-buttons-container h3, .show-buttons-container h4 {
  margin: 0 30 5px 0;
}
.show-buttons-container p {
  margin-bottom: 5px;
}
.buttons {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 5px;
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
