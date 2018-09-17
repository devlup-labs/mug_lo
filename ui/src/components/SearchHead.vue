<template>
<v-container grid-list-md>
<v-layout row wrap>

<v-btn flat round style="font-size:15pt;" class="blue--text">
        Your Search Results...
      </v-btn>
<v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-center headline blue--text" pt-5 ><h5>Books</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in books" :key="i" px-2 py-0>
                <a link :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </a>
              </v-flex>
            </v-container>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-center headline blue--text" pt-5 ><h5>Assignments</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in assignments" :key="i" px-2 py-0>
                <a link :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </a>
              </v-flex>
            </v-container>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout pb-1 pt-1 >
      <v-flex >
        <v-container>
          <v-card >
            <v-card-text :class=colorScheme class="text-xs-left headline blue--text" pt-5 ><h5>Notes</h5></v-card-text>
          </v-card>
          <v-card>  
            <v-container class="scrolling-wrapper-flexbox " id="cardContainer">
              <v-flex v-for="(item,i) in notes" :key="i" px-2 py-0>
                <a link :color=colorScheme>
                  <v-card v-bind:style="{ 'background-image': 'url(' + item.src + ')' }" class="card">
                    <v-card-media height=200px class="mask1">
                      <v-layout align-end justify-center>
                        <h3 class="white--text"><bold><center>Digital Logic and Design</center></bold></h3>
                      </v-layout>
                    </v-card-media>
                  </v-card>
                </a>
              </v-flex>
            </v-container>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
</v-flex>
</v-layout>
</v-container>
</template>

<script>
  import {
    VCard,
    VBtn,
    VIcon,
    VSelect
  } from 'vuetify'

  export default {
    name: 'search-head',
    components: {
      VCard,
      VBtn,
      VIcon,
      VSelect
    },
    data: () => ({
      items: ['Name', 'Date'],
      books: [
        {title: 'Book1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ],
      notes: [
        {title: 'Notes1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Notes2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Notes3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Book3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ],
      assignments: [
        {title: 'Tutorial 1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Assignment 1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Assignment 2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Tutorial 1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Assignment 1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
        {title: 'Assignment 2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
      ]
    })
}
</script>
<style>
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