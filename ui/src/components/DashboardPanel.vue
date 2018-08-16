<template>
<div>
<v-layout row wrap>
    <v-flex xs6 offset-sm0  pa-2>
      <v-card>
       <v-card-title><span class="blue--text">Bookmarks</span></v-card-title>
    <v-layout row wrap>
    <v-flex v-for="item in Bookmarks" pa-2>
    <v-card>
    <v-card-media :src="item.src" height="150px">
                </v-card-media>
                 <v-layout justify-center>
                   <v-card-actions>
                     <v-btn primary round color="info">
                    {{item.title}}
                  </v-btn>
                </v-card-actions>
             </v-layout>
       </v-card>
    </v-flex>
   </v-layout>
       <v-layout justify-end><v-card-actions><v-btn primary round color="info">View More</v-btn></v-card-actions></v-layout>
       </v-card>
 </v-flex>
 <v-flex xs6 offset-sm0  pa-2>
      <v-card>
       <v-card-title><span class="blue--text">Recently Uploaded</span></v-card-title>
    <v-layout row wrap>
    <v-flex v-for="item in Uploads" pa-2>
    <v-card>
    <v-card-media :src="item.src" height="150px">
                </v-card-media>
                 <v-layout justify-center>
                   <v-card-actions>
                     <v-btn primary round color="info">
                    {{item.title}}
                  </v-btn>
                </v-card-actions>
             </v-layout>
       </v-card>
    </v-flex>
   </v-layout>
<v-layout justify-end><v-card-actions><v-btn primary round color="info">View More</v-btn></v-card-actions></v-layout>
       </v-card>
 </v-flex>
 </v-layout>
 <v-layout row wrap>
 <v-flex xs12 offset-sm0  pa-2>
      <v-card>
       <v-card-title><span class="blue--text">Your Courses</span></v-card-title>
    <v-layout row wrap>
    <v-flex v-for="item in Courses" pa-2>
    <v-card>
    <v-card-media :src="item.src" height="150px">
                </v-card-media>
                 <v-layout justify-center>
                   <v-card-actions>
                     <v-btn primary round color="info">
                    {{item.title}}
                  </v-btn>
                </v-card-actions>
             </v-layout>
       </v-card>
    </v-flex>
   </v-layout>
<v-layout justify-end><v-card-actions><v-btn primary round color="info">View More</v-btn></v-card-actions></v-layout>
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
 import {mapGetters} from 'vuex'

 export default {
   name: 'dashboard-head',
   components: {
     VCard,
     VBtn,
     VIcon
   },
   data: () => ({
     Bookmarks: [
       {title: 'Book1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Book2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Book3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
     ],
     Uploads: [
       {title: 'Upload1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Upload2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Upload3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
     ],
     Courses: [
       {title: 'Course1', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Course2', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Course3', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Course4', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Course5', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'},
       {title: 'Course6', src: 'https://images-na.ssl-images-amazon.com/images/I/81OnFXKcHKL.jpg'}
     ]
   }),
   computed: {
     ...mapGetters('config', {
       BACKEND_API_ADDRESS: 'BACKEND_API_ADDRESS'
     })
   }
 }
</script>
<style scoped>
a {
    text-decoration: none;
  }
</style>
