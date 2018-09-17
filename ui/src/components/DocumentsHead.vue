<template>
  <div>
    <v-layout>
      <v-flex>
        <v-card style="background-color:white" >
          <v-card-text :style="{'background-color':colorScheme}"><div class="headline primary-title white--text">Books</div></v-card-text>
          <v-container id="scroll-target" style="max-height:800px" class="scroll-y">
            <br>
            <v-layout v-scroll:#scroll-target="onScroll"  wrap>
              <v-flex v-for="(item,i) in courses" :key="i" pa-2>
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
          </v-container>
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
  name: 'documents-head',
  components: {
    VCard,
    VBtn,
    VIcon
  },
  data () {
    return {
      windowHeight: 0,
      colorScheme: '#1E88E5',
      courses: [
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ]
    }
  },
  mounted () {
    this.$nextTick(() => {
      window.addEventListener('resize', () => {
        this.windowHeight = window.innerHeight
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

</style>
