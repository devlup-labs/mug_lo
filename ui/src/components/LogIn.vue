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
                <div>
                  Sign in with:
                  <router-link to="/signin">
                    <v-avatar>
                      <div id="gicon">
                        <img src="http://icons.iconarchive.com/icons/danleech/simple/1024/google-icon.png"
                             width="25px"
                             height="25px"/>
                      </div>
                    </v-avatar>
                  </router-link>
                </div>
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
    VBtn
  } from 'vuetify'

  export default {
    name: 'LogIn',
    components: {
      VCard,
      VCheckbox,
      VTextField,
      VForm,
      VBtn
    }
  }
</script>
