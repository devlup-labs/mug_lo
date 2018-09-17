<template>
  <div>
    <v-layout row wrap>
      <v-flex md6 xs12 offset-sm0 pa-2>
        <v-card  style="background-color:white" >
          <center><v-card-text :style="{'background-color':colorScheme}"><div class="headline primary-title white--text">Bookmarks</div></v-card-text></center>
          <v-layout row wrap>
            <v-flex v-for="(item,i) in bookmarks" :key="i" pa-2 xs4>
              <router-link to='/dashboard' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card" >
                    <v-card-media height=200px class="mask1" >
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
            </v-flex>
          </v-layout>
           <v-layout justify-end>
            <v-card-actions>
              <router-link to='/coursecontents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
        </v-card>
      </v-flex>
      <v-flex md6 xs12  offset-sm0 pa-2 >
        <v-card>
          <center><v-card-text :style="{'background-color':colorScheme}"><div class="headline primary-title white--text">Recently Uploaded</div></v-card-text></center>
          <v-layout row wrap>
            <v-flex v-for="(item,i) in uploads" :key="i" pa-2 xs4>
              <router-link to='/dashboard' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
            </v-flex>
          </v-layout>
           <v-layout justify-end>
            <v-card-actions>
              <router-link to='/coursecontents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 offset-sm0 pa-2>
        <v-card>
          <center><v-card-text :style="{'background-color':colorScheme}"><div class="headline primary-title white--text">Your Courses</div></v-card-text></center>
          <v-layout row wrap>
            <v-flex v-for="(item,i) in courses" :key="i" pa-2 xs4 md2>
              <router-link to='/dashboard' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
            </v-flex>
          </v-layout>
          <v-layout justify-end>
            <v-card-actions>
              <router-link to='/coursecontents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import {
    VCard,
    VBtn,
    VIcon
  } from 'vuetify'

  export default {
    name: 'dashboard-head',
    components: {
      VCard,
      VBtn,
      VIcon
    },
    data () {
      return {
        colorScheme: '#1E88E5',
        bookmarks: [
          {title: 'Book1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Book2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Book3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
        ],
        uploads: [
          {title: 'Upload1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Upload2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Upload3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
        ],
        courses: [
          {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
          {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
        ]
      }
    }
  }
</script>
<style scoped>
  a {
    text-decoration: none;
  }
  .card {
    flex: 0 0 auto;
    
    background-size:cover;
    height:200px;
  }
.mask1 {
  background: linear-gradient(to top,black 1%, transparent);
  opacity:0.75; 
}
</style>
