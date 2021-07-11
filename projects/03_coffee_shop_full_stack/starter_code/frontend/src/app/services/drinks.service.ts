import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';
import { ToastController } from '@ionic/angular';

export interface Drink {
  id: number;
  title: string;
  recipe: Array<{
    name: string,
    color: string,
    parts: number
  }>;
}

@Injectable({
  providedIn: 'root'
})
export class DrinksService {
  url = environment.apiServerUrl;
  public items: { [key: number]: Drink } = {};

  constructor(private auth: AuthService, private http: HttpClient, public toastController: ToastController) { }

  getHeaders() {
    return { headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.activeJWT()}`) };
  }

  getDrinks() {
    const url = `${this.url}${this.auth.can('get:drinks-detail') ? '/drinks-detail' : '/drinks'}`;
    this.http.get(url, this.getHeaders())
    .subscribe((res: any) => {
      if (res.success) {
        for (const drink of res.drinks) {
          this.items[drink.id] = drink;
        }
      }
    },
    error => this.showToast(true, error.error.message));
  }

  saveDrink(drink: Drink) {
    if (drink.id >= 0) { // patch
      this.http.patch(this.url + '/drinks/' + drink.id, drink, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.items[drink.id] = res.drink;
            this.showToast(false, 'Drink updated');
          }
        },
        error => this.showToast(true, error.error.message));
    } else { // insert
      this.http.post(this.url + '/drinks', drink, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.items[res.drink.id] = res.drink;
            this.showToast(false, 'Drink created');
          }
        },
        error => this.showToast(true, error.error.message));
    }

  }

  deleteDrink(drink: Drink) {
    this.http.delete(this.url + '/drinks/' + drink.id, this.getHeaders())
      .subscribe((res: any) => {
        if (res.success) {
          delete this.items[res.id];
          this.showToast(false, 'Drink deleted');
        }
      },
      error => this.showToast(true, error.error.message));
  }

  async showToast(isError: boolean, message: string) {
    const toast = await this.toastController.create({
      message: message,
      color: isError ? "danger" : "success",
      position: 'middle',
      duration: 2000
    });
    toast.present();
  }
}
