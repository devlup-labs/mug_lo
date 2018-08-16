<template>
  <v-container grid-list-lg>
    <v-layout column>
      <v-flex>
        <v-card>
          <v-container
            fluid>
            <v-card-title primary-title>
              <span class="display-10 blue--text">Login</span>
            </v-card-title>
            <v-form>
              <v-text-field prepend-icon="person" name="Username" label="Username"></v-text-field>
              <v-text-field prepend-icon="lock" name="Password" label="Password" type="password"></v-text-field>
              <v-flex>
                <v-layout align-center justify-space-around wrap>
                  <v-checkbox label="Remember me"></v-checkbox>
                  <v-spacer></v-spacer>
                  <router-link to="password-reset">
                    <span class="blue--text"> Forgot Password?</span>
                  </router-link>
                </v-layout>
              </v-flex>
            </v-form>
            <v-card-actions>
              <v-btn primary round large block color="info">Login</v-btn>
            </v-card-actions>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {
    VCard,
    VTextField,
    VCheckbox,
    VForm,
    VBtn,
    VIcon
  } from 'vuetify'
  import {mapGetters} from 'vuex'

  export default {
    name: 'login-panel',
    components: {
      VCard,
      VCheckbox,
      VTextField,
      VForm,
      VBtn,
      VIcon
    },
    computed: {
      ...mapGetters('config', {
        BACKEND_API_ADDRESS: 'BACKEND_API_ADDRESS'
      }),
      googleSignInUrl () {
        return this.BACKEND_API_ADDRESS + '/login/google-oauth2'
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>
