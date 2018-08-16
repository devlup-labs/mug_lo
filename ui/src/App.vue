<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title v-text="title" class="blue--text"></v-toolbar-title>
    <v-spacer></v-spacer>
    <div class="row align-center">     
<v-toolbar-items class="hidden-sm-and-down">
      <v-btn round flat class="blue--text">Dashboard</v-btn>
      <v-btn round flat class="blue--text">Upload</v-btn>
      <v-btn round flat class="blue--text">My Docs</v-btn>
      <v-divider vertical></v-divider>
      <v-text-field placeholder="Search" append-icon="search" solo class="pr-4"></v-text-field>
       <v-content> </v-content>
       <v-btn fab dark color="blue">
              <v-icon>account_circle</v-icon>
            </v-btn>
       
</v-toolbar-items>
 </div> 
   </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
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
