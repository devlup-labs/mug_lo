<template>
   <v-container text-xs-left>
    <v-layout row wrap>
      <v-flex xs12 v-for="(item,i) in courseDetails" :key="i" pa-2 row>
      <v-card>
        <v-card-text class="purple"></v-card-text>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{item.courseName}} ({{item.courseCode}})</div>
            <span class="grey--text">{{item.prof}}</span>
          </div>
        </v-card-title>

        <v-layout row wrap justify-end>
            <router-link to='/coursedetails'><v-btn flat>Explore Course Details</v-btn></router-link>
            <router-link to='/coursecontents'><v-btn flat color="purple">Explore Course Materials </v-btn></router-link>
        </v-layout> 
      </v-card>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import {
  VCard,
  VBtn,
  VIcon
} from 'vuetify'

export default {
  name: 'my-courses-head',
  components: {
    VCard,
    VBtn,
    VIcon
  },
  data () {
    return {
      windowHeight: 0,
      windowWidth: 1280,
      courseDetails: [
        {'courseName': 'Signals and Systems', 'courseCode': 'EE213', 'prof': 'Dr. Rajlaxmi Chouhan'},
        {'courseName': 'Basic Electrical Engineering', 'courseCode': 'EE211', 'prof': 'Dr. Deepak Fulwani'},
        {'courseName': 'Data Structure and Algorithms', 'courseCode': 'CS121', 'prof': 'Dr. Sumit Kalra'},
        {'courseName': 'Object Oriented Analysis and Design', 'courseCode': 'CS212', 'prof': 'Dr. Subhajit Sidhanta'},
        {'courseName': 'Digital Logic and Design', 'courseCode': 'CS211', 'prof': 'Dr. Akhl Garg'},
        {'courseName': 'Economics', 'courseCode': 'EE213', 'prof': 'Dr. ABC XYZ'}
      ]
    }
  },
  mounted () {
    this.$nextTick(() => {
      window.addEventListener('resize', () => {
        this.windowHeight = window.innerHeight
        this.windowWidth = window.innerWidth
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
.btn {
white-space:normal !important;
word-wrap:break-word;
}

</style>
