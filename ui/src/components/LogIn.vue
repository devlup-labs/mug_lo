<template>
  <v-container align-center justify-center fill-height>
    <v-flex column xs3 text-xs-center>
      <v-container grid-list-lg>
        <v-layout column>
          <v-flex>
            <v-card>
              <v-container
                fluid>
                <v-card-title primary-title>
                  <span class="display-1 blue--text">Login</span>
                </v-card-title>
                <v-form>
                  <v-text-field prepend-icon="person" name="Username" label="Username"></v-text-field>
                  <v-text-field prepend-icon="lock" name="Password" label="Password" type="password"></v-text-field>
                  <v-flex>
                    <v-layout align-center justify-space-around wrap>
                      <v-checkbox label="Remember me"></v-checkbox>
                      <v-spacer></v-spacer>
                      <router-link to="/forgotpass">
                        <span class="blue--text"> Forgot Password?</span>
                      </router-link>
                    </v-layout>
                  </v-flex>
                </v-form>
                <v-card-actions>
                  <v-btn primary large block color="info">Login</v-btn>
                </v-card-actions>
              </v-container>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card>
              <v-card-title primary-title>
                <v-flex row justify-center>
                  <div>Sign in with:</div>
                  <router-link to="/signin">
                    <v-icon medium color="red darken-3">fa-google-plus</v-icon>
                  </router-link>
                </v-flex>
              </v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-flex>
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

  export default {
    name: 'LogIn',
    components: {
      VCard,
      VCheckbox,
      VTextField,
      VForm,
      VBtn,
      VIcon
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>
