<template>
  <div >

    <v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-center headline white--text" pt-5 ><h5>Bookmarks</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in books" :key="i" px-2 py-0>
                <router-link to='#' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
              </v-flex>

            </v-container>
            <v-layout justify-end>
            <v-card-actions>
              <router-link to='/documents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-center headline white--text" pt-5 ><h5>Assignments</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in books" :key="i" px-2 py-0>
                <router-link to='#' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
              </v-flex>
            </v-container>
            <v-layout justify-end>
            <v-card-actions>
              <router-link to='/documents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-center headline white--text" pt-5 ><h5>Notes</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in books" :key="i" px-2 py-0>
                <router-link to='#' :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </router-link>
              </v-flex>
            </v-container>
            <v-layout justify-end>
            <v-card-actions>
              <router-link to='/documents'><v-btn primary round color="info">View More</v-btn>
              </router-link>
            </v-card-actions>
          </v-layout>
          </v-card>
        </v-container>
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
  name: 'course-contents-head',
  components: {
    VCard,
    VBtn,
    VIcon
  },
  data () {
    return {
      windowHeight: 0,
      textHeight: 0,
      colorScheme: 'blue',
      books: [
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5fsfsdfdsfadsfasdfas asdfa sdfasdfasd', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ],
      assignments: [
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ],
      notes: [
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ]
    }
  },
  mounted () {
    this.$nextTick(() => {
      window.addEventListener('resize', () => {
        this.windowHeight = window.innerHeight
      })
      window.addEventListener('resize', () => {
        this.textHeight = document.getElementById('cardContainer').style.height - document.getElementById('text').style.height
      })
    })
  },
  computed: {
    myStyles () {
      return {
        height: 400
      }
    }
  }
}
</script>
<style scoped>
a {
  text-decoration: none;
}
.scrolling-wrapper-flexbox {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;

 
}
.card {
    flex: 0 0 auto;
    min-width:150px;
    max-width:150px; 
    background-size:cover;
    height:200px;
  }
.mask1 {
  background: linear-gradient(to top,black 1%, transparent);
  opacity:0.75; 
}
.cover {object-fit: cover;}


</style>
