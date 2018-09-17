<template>
 <v-container grid-list-lg>
 <v-layout row wrap>
 <v-flex xs12 >
 <v-container>
 <v-layout row wrap>
 <v-content><span style="font-size:15pt">Course code: {{code}}</span></v-content>
 <v-content><span style="font-size:15pt">Course name: {{name}}</span></v-content>
 <v-content><span style="font-size:15pt">Professor: {{prof}}</span></v-content>
 <v-content><span style="font-size:15pt">L-T-P: {{distribution.lectures}}-{{distribution.tutorials}}-{{distribution.practicals}} </span></v-content>
 </v-layout>
 </v-container>
 </v-flex>
 <v-flex xs8>
  <v-layout row wrap>
  <v-content><span style="font-size:15pt" class="blue--text">Syllabus: </span></v-content>
  <v-textarea solo readonly v-model="syllabus" height="250"style="width: 600px;"></v-textarea>
  </v-layout>
 </v-flex>
  <v-flex xs4 pl-4>
  <v-layout row wrap>
  <v-content><span style="font-size:14pt" class="blue--text">Marks Distribution:</span></v-content>
    <v-data-table hide-headers hide-actions :items="marks_dis">
    <template slot="items" slot-scope="props">
    <td>{{ props.item.name }}</td>
   <td>{{ props.item.dis }}%</td>
    </template>
</v-data-table>
  </v-layout>
 </v-flex>
 <v-flex xs6>
 <v-content><span class="blue--text" style="font-size:14pt">Books recommended:</span></v-content>
 <v-data-table hide-headers hide-actions :items="books">
  <template slot="items" slot-scope="props">
    <td>{{ props.item }}</td>
    </template>
 </v-data-table>
 </v-flex>
 <v-flex xs6 pa-4>
 <v-container grid-list-lg>
  <v-card>
  <v-card-title><span class="blue--text"style="font-size:14pt">Professor Details</span></v-card-title>
   <v-flex xs12 pa-3>
   <v-layout row wrap align-center>
   <v-content><span style="font-size:15pt">Email:</span></v-content>
   <v-text-field v-model="email" solo readonly></v-text-field>
   </v-layout>
   </v-flex>
   <v-flex xs12 pa-3>
   <v-layout row wrap align-center>
   <v-content><span style="font-size:15pt">Office Address:</span></v-content>
   <v-textarea v-model="office" readonly solo style="width:300px;"></v-textarea>
</v-layout>
    </v-flex>
  </v-card>
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
   VDataTable,
   VTextarea,
   VInput
} from 'vuetify'
export default {
   name: 'course-details',
   components: {
     VCard,
     VBtn,
     VTextField,
     VTextarea,
     VDataTable,
     VInput
   },
   data: () => ({
     code: 'EE213',
     name: 'Signal & Systems',
     prof: 'Dr. Rajlaxmi Chouhan',
     distribution: {lectures: '3', tutorials: '1', practicals: '0'},
     syllabus: 'main contents of course',
     marks_dis: [
       {name: 'Mid-Sem I', dis: '10'},
       {name: 'Mid-Sem II', dis: '10'},
       {name: 'End-Sem', dis: '40'},
       {name: 'Lab', dis: '20'},
       {name: 'Quiz', dis: '10'},
       {name: 'Assignments', dis: '10'}
     ],
     books: ['book1', 'book2', 'book3', 'book4', 'book5'],
     office: 'address',
     email: 'prof@iitj.ac.in'
   })
}
</script>
