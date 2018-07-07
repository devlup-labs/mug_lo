<template>
  <div id="main">
  <v-container>
    <v-layout column align-center row class="text-xs-center">
      <v-flex xs4 class="white">
        <v-container style="position: relative;top: 13%;" class="text-xs-center">
          <div style="width: 300px">
          <v-card >
            <v-card-title primary-title>
              <h4>Login</h4>
            </v-card-title>
            <v-form>
              <v-text-field prepend-icon="person" name="Username" label="Username"></v-text-field>
              <v-text-field prepend-icon="lock" name="Password" label="Password" type="password"></v-text-field>
              <v-flex>
                <v-layout align-center justify-space-around wrap>
                <v-checkbox label="Remember me"></v-checkbox>
                  <router-link to="/forgotpass"><div style="color: #0d47a1"> Forgot Password ?</div></router-link>
              </v-layout>
              </v-flex>
              <v-card-actions>
                  <v-btn primary large block color="btncolor">Login</v-btn>
              </v-card-actions>
            </v-form>
          </v-card>
          </div>
        </v-container>
      </v-flex>
    </v-layout>
  </v-container>
    <v-container>
      <v-layout column align-center>
    <v-flex class="white" xs4>
      <v-container>
      <v-card>
        <v-layout align-center wrap>
    <v-layout align-center wrap>
      <div id="signtitle">Sign in with:</div>
      <router-link to="/signin">
      <v-avatar>
        <div id="gicon">
        <img  src="http://icons.iconarchive.com/icons/danleech/simple/1024/google-icon.png" width="25px" height="25px"/>
        </div>
      </v-avatar>
      </router-link>
    </v-layout>
    </v-layout>
        </v-card>
      </v-container>
    </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
    export default {
      name: 'LogIn'
    }
</script>

<style scoped>
  h4{
    color: #2196f3;
    font-size: 25px;
  }
#main{
  background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuVB_E4knVRLubs6xlrb8FveXkahbBWBMiGEqXuhX0Vk6GB1rI");
  background-size: cover;
  background-repeat: no-repeat;
  height: 100%;
}
  #signtitle{
    font-size: 20px;
  }
  #gicon{
    position: relative;
    top: 5px;
    padding-left: 10px;
  }

</style>
