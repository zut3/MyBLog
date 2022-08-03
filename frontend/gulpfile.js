const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'))
const browser = require('browser-sync').create()

function style() {
    return gulp.src('./src/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('../static/css'))
        .pipe(browser.stream())
}

function watch() {
    browser.init({
        server : {
            baseDir: './public'
        }
    })

    gulp.watch('./src/*.scss', style)
    gulp.watch('./public/*.html').on('change', browser.reload)
    gulp.watch('./public/**/*.js').on('change', browser.reload)
}

exports.watch = watch;
exports.style = style;
exports.default = watch;

