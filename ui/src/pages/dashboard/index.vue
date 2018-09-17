<template>
  <v-container>
    <v-flex>
      <dashboard-head/>
    </v-flex>
  </v-container>
</template>

<script>
 import DashboardHead from '../../components/DashboardHead'
 export default {
   name: 'Dashboard',
   components: {
     DashboardHead
   }
 }
</script>
