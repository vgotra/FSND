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
import { GenreComponent } from './pages/genre/genre.component';
import { GenreStoreService } from './pages/genre/genre.store.service';
import { GenresComponent } from './pages/genres/genres.component';
import { GenresStoreService } from './pages/genres/genres.store.service';
import { LanguageComponent } from './pages/language/language.component';
import { LanguageStoreService } from './pages/language/language.store.service';
import { LanguagesComponent } from './pages/languages/languages.component';
import { LanguagesStoreService } from './pages/languages/languages.store.service';
import { NotFoundComponent } from './common/components/not-found/not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    ActorsComponent,
    ActorComponent,
    MoviesComponent,
    MovieComponent,
    GenresComponent,
    GenreComponent,
    LanguagesComponent,
    LanguageComponent,
    NotFoundComponent
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
    GenresStoreService,
    GenreStoreService,
    LanguagesStoreService,
    LanguageStoreService,
    { provide: HTTP_INTERCEPTORS, useClass: RequestInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
