<template>
  <v-container>
    <v-flex>
      <course-contents-head/>
    </v-flex>
  </v-container>
</template>

<script>
 import CourseContentsHead from '../../components/CourseContentsHead'
 export default {
   name: 'CourseContents',
   components: {
     CourseContentsHead
   }
 }
</script>
