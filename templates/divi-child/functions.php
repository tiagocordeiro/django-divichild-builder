<?php
/**
 *
 * Mulher Gorila
 *
 * @package WordPress
 * @subpackage Mulher Gorila Themes
 * @author Mulher Gorila <tiago@mulhergorila.com>
 * Divi Child Theme functions.php
 *
 * ===== NOTES ==================================================================
 * 
 * Unlike style.css, the functions.php of a child theme does not override its 
 * counterpart from the parent. Instead, it is loaded in addition to the parent's 
 * functions.php. (Specifically, it is loaded right before the parent's file.)
 * 
 * In that way, the functions.php of a child theme provides a smart, trouble-free 
 * method of modifying the functionality of a parent theme.
 * 
 * =============================================================================== */
 
function divichild_enqueue_styles() {
  
	$parent_style = 'parent-style';

	wp_enqueue_style( $parent_style, get_template_directory_uri() . '/style.css' );
	wp_enqueue_style( 'child-style',
		get_stylesheet_directory_uri() . '/style.css',
		array( $parent_style ),
		wp_get_theme()->get('Version')
	);
}
add_action( 'wp_enqueue_scripts', 'divichild_enqueue_styles' );

// Custom WordPress Footer
function remove_footer_admin () {
	echo '&copy; '.date("Y").' - Mulher Gorila';
}
add_filter('admin_footer_text', 'remove_footer_admin');

// Use your own external URL logo link
function wpc_url_login(){
	return "{{customer_site}}"; // your URL here
}
add_filter('login_headerurl', 'wpc_url_login');

add_action( 'admin_bar_menu', 'remove_wp_logo', 999 );

function remove_wp_logo( $wp_admin_bar ) {
	$wp_admin_bar->remove_node( 'wp-logo' );
}