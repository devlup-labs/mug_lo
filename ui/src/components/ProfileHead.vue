<template>
  <v-container grid-list-lg>
   <v-layout row wrap>
    <v-flex xs12 sm12> 
      <v-layout justify-center><span style="font-size:25pt">USER PROFILE</span></v-layout>
    </v-flex>
    <v-flex xs12 sm6>
     <v-layout justify-center column wrap>
     <v-avatar :size="256">
       <img class="profilepicture" src="https://cdn.vuetifyjs.com/images/john.jpg">
     </v-avatar>
     <v-layout justify-center column>
     <v-container grid-list-lg>
      <v-flex  xs0 offset-sm0>
       <v-chip color="info" text-color="white"><span style="font-size:25pt">{{ name }}</span></v-chip>
      </v-flex>
     </v-container>
    </v-layout>
    </v-layout>
   </v-flex>
   <v-flex xs12 sm6>
   <v-container grid-list-lg>
    <v-layout row wrap>
     <v-flex xs6>
      <v-content><span style="font-size:20pt">Email ID</span></v-content>
     </v-flex>
    <v-flex xs6> 
     <v-text-field v-model="email" solo readonly></v-text-field>
    </v-flex>
     <v-flex xs6>
      <v-content><span style="font-size:20pt">Roll Number</span></v-content>
     </v-flex>
    <v-flex xs6> 
     <v-text-field v-model="rollno" solo readonly></v-text-field>
    </v-flex>
    <v-flex xs6>
      <v-content><span style="font-size:20pt">Your Courses</span></v-content>
     </v-flex>
    <v-flex xs6> 
    <v-data-table hide-headers hide-actions :items="courses">
    <template slot="items" slot-scope="props">
    <td>{{ props.item }}</td>
    </template>
   </v-data-table>
    </v-flex>
   </v-layout>
   </v-container>
   </v-flex>
 
</v-layout>
 </v-container>
</template>


<script>
   import {
     VCard,
     VBtn,
     VTextField,
     VChip,
     VDataTable,
     VInput
} from 'vuetify'

export default {
     name: 'profile-head',
     components: {
       VCard,
       VBtn,
       VTextField,
       VChip,
       VDataTable,
       VInput
     },
     data: () => ({
       profilepic: 'img.png',
       name: 'John Taylor',
       bio: 'your-bio',
       email: 'example@iitj.ac.in',
       rollno: 'B17EE050',
       courses: ['course1', 'course2', 'course3', 'course4', 'course5', 'course6']
  })

}
</script>
<style>
 .profilepicture{
   border-radius:0
 }
</style>
