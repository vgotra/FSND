import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AuthModule } from '@auth0/auth0-angular';
import { ActorsComponent } from './pages/actors/actors.component';
import { ActorComponent } from './pages/actor/actor.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RequestInterceptor } from './common/interceptors/http.interceptor';
import { AuthInterceptor } from './common/interceptors/auth.interceptor';
import { ActorsStoreService } from './pages/actors/actors.store.service';
import { ActorStoreService } from './pages/actor/actor.store.service';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MaterialModule } from './material.module';
import { MoviesStoreService } from './pages/movies/movies.store.service';
import { MovieStoreService } from './pages/movie/movie.store.service';
import { MovieComponent } from './pages/movie/movie.component';
import { MoviesComponent } from './pages/movies/movies.component';

@NgModule({
  declarations: [
    AppComponent,
    ActorsComponent,
    ActorComponent,
    MoviesComponent,
    MovieComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AuthModule.forRoot({
      domain: 'dev-fsnd-capstone-agency.eu.auth0.com',
      clientId: 'og3O1MANqyolsad7yaxonr4OWhCjb5hm'
    }),
    AppRoutingModule,
    MaterialModule,
    BrowserAnimationsModule,
    FlexLayoutModule
  ],
  providers: [
    ActorsStoreService,
    ActorStoreService,
    MoviesStoreService,
    MovieStoreService,
    { provide: HTTP_INTERCEPTORS, useClass: RequestInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
