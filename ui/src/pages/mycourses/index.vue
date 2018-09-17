<template>
  <v-container>
    <v-flex>
      <my-courses-head/>
    </v-flex>
  </v-container>
</template>

<script>
 import MyCoursesHead from '../../components/MyCoursesHead'
 export default {
   name: 'MyCourses',
   components: {
     MyCoursesHead
   }
 }
</script>
