<template>
  <v-app v-bind:style="{ 'background-color': colorScheme,'background': 'url(https://image.freepik.com/free-vector/seamless-pattern-tile_1159-5367.jpg)'}">
    <v-toolbar :style="{'background-color':toolbarcolor}" class="cover">
      <v-toolbar-title v-text="title" :style="{color:toolbartextcolor}"></v-toolbar-title>
    <v-spacer></v-spacer>
    <div class="row align-center">     
<v-toolbar-items class="hidden-sm-and-down">
      <v-btn round flat>
        <router-link to="/dashboard" :style="{color:toolbartextcolor}">Dashboard</router-link></v-btn>
      <v-btn round flat>
        <router-link to="/upload" :style="{color:toolbartextcolor}">Upload</router-link></v-btn>
        <v-btn round flat>
        <router-link to="/mycourses" :style="{color:toolbartextcolor}">My Courses</router-link></v-btn>
      <v-divider vertical></v-divider>
      <v-text-field placeholder="Search" append-icon="search" solo class="pr-4"></v-text-field>
       <v-content> </v-content>
       <v-btn fab dark color="blue darken-1">
              <v-icon>account_circle</v-icon>
            </v-btn>
       
</v-toolbar-items>
 </div> 
   </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      colorScheme: 'white',
      toolbartextcolor: '#1E88E5',
      toolbarcolor: 'white',
      items: [{
        icon: 'bubble_chart',
        title: 'Inspire'
      }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Mug Lo'
    }
  },
  name: 'App'
}
 </script>

 <style>
.cover {object-fit: cover;}

 </style>
