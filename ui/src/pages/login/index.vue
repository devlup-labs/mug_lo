<template>
  <v-container align-center justify-center fill-height>
    <v-flex column sm6 md6 lg4 text-xs-center>
      <login-panel/>
    </v-flex>
  </v-container>
</template>

<script>
  import LoginPanel from '../../components/LoginPanel'

  export default {
    name: 'LogIn',
    components: {
      LoginPanel
    }
  }
</script>
