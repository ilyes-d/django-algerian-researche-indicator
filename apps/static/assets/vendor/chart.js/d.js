var __decorate=this&&this.__decorate||function(t,e,i,r){var a,n=arguments.length,o=n<3?e:null===r?r=Object.getOwnPropertyDescriptor(e,i):r;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)o=Reflect.decorate(t,e,i,r);else for(var h=t.length-1;h>=0;h--)(a=t[h])&&(o=(n<3?a(o):n>3?a(e,i,o):a(e,i))||o);return n>3&&o&&Object.defineProperty(e,i,o),o};import{NgModule,Component,ElementRef,AfterViewInit,OnDestroy,Input,Output,EventEmitter,ChangeDetectionStrategy}from"@angular/core";import{CommonModule}from"@angular/common";import*as Chart from"chart.js";let UIChart=class{constructor(t){this.el=t,this.options={},this.plugins=[],this.responsive=!0,this.onDataSelect=new EventEmitter}get data(){return this._data}set data(t){this._data=t,this.reinit()}ngAfterViewInit(){this.initChart(),this.initialized=!0}onCanvasClick(t){if(this.chart){let e=this.chart.getElementAtEvent(t),i=this.chart.getDatasetAtEvent(t);e&&e[0]&&i&&this.onDataSelect.emit({originalEvent:t,element:e[0],dataset:i})}}initChart(){let t=this.options||{};t.responsive=this.responsive,t.responsive&&(this.height||this.width)&&(t.maintainAspectRatio=!1),this.chart=new Chart(this.el.nativeElement.children[0].children[0],{type:this.type,data:this.data,options:this.options,plugins:this.plugins})}getCanvas(){return this.el.nativeElement.children[0].children[0]}getBase64Image(){return this.chart.toBase64Image()}generateLegend(){if(this.chart)return this.chart.generateLegend()}refresh(){this.chart&&this.chart.update()}reinit(){this.chart&&(this.chart.destroy(),this.initChart())}ngOnDestroy(){this.chart&&(this.chart.destroy(),this.initialized=!1,this.chart=null)}};UIChart.ctorParameters=(()=>[{type:ElementRef}]),__decorate([Input()],UIChart.prototype,"type",void 0),__decorate([Input()],UIChart.prototype,"options",void 0),__decorate([Input()],UIChart.prototype,"plugins",void 0),__decorate([Input()],UIChart.prototype,"width",void 0),__decorate([Input()],UIChart.prototype,"height",void 0),__decorate([Input()],UIChart.prototype,"responsive",void 0),__decorate([Output()],UIChart.prototype,"onDataSelect",void 0),__decorate([Input()],UIChart.prototype,"data",null);export{UIChart};let ChartModule=class{};ChartModule=__decorate([NgModule({imports:[CommonModule],exports:[UIChart=__decorate([Component({selector:"p-chart",template:'\n        <div style="position:relative" [style.width]="responsive && !width ? null : width" [style.height]="responsive && !height ? null : height">\n            <canvas [attr.width]="responsive && !width ? null : width" [attr.height]="responsive && !height ? null : height" (click)="onCanvasClick($event)"></canvas>\n        </div>\n    ',changeDetection:ChangeDetectionStrategy.Default})],UIChart)],declarations:[UIChart]})],ChartModule);export{ChartModule};