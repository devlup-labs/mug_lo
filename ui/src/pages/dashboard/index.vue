<template>
  <v-container>
    <v-flex>
      <dashboard-head/>
    </v-flex>
  </v-container>
</template>

<script>
 import DashboardPanel from '../../components/DashboardPanel'
 export default {
   name: 'Dashboard',
   components: {
     DashboardPanel
   }
 }
</script>
