<template>
<v-layout>
<v-container>
<v-container grid-list-lg>
    <v-layout align-center column>
     <v-flex>
        <v-card>
         <v-container fluid>
            <v-layout justify-center column fill-height>
            <v-card-title primary-title>
              <span class="headline blue--text">Upload your files here</span>
            </v-card-title>
            <v-card-actions>
             <v-btn primary round large block color="info">Upload from Device</v-btn>
    </v-card-actions>
  
  <v-card-text><v-layout justify-center>OR</v-layout></v-card-text>
  <v-card-actions>
             <v-btn primary round large block color="info">Upload from Drive</v-btn>
    </v-card-actions>
            </v-layout>
</v-container>
</v-card>
</v-flex>
</v-layout>
</v-container>
</v-container>
</v-layout>
</template>
 
<script>
import {
  VBtn,
  VCard
} from 'vuetify'
import {mapGetters} from 'vuex'
export default{
  name: 'upload-head',
  components: {
    VBtn,
    VCard
  },
  computed: {
    ...mapGetters('config', {
      BACKEND_API_ADDRESS: 'BACKEND_API_ADDRESS'
    })
  }
}
</script>
